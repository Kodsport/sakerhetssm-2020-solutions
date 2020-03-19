#include <stdio.h>
#include <string.h>

#include "sodium.h"

#define ELF_MAGIC_BYTES 0x464c457f

#pragma pack(push)
#pragma pack(1)
typedef struct {
    uint8_t ident[16];
    uint16_t type;
    uint16_t machine;
    uint32_t version;
    uint64_t start_address;
    uint64_t program_header_offset;
    uint64_t section_header_offset;
    uint32_t flags;
    uint16_t header_size;
    uint16_t phentsize;
    uint16_t phnum;
    uint16_t shentsize;
    uint16_t shnum;
    uint16_t shtrndx;
} elf_header;

typedef struct {
    uint32_t type;
    uint32_t flags;
    uint64_t offset;
    uint64_t vaddr;
    uint64_t paddr;
    uint64_t filesz;
    uint64_t memsz;
    uint64_t align;
} program_header;

typedef struct {
    uint8_t signature[64];
    char name[32];
    uint32_t max_message_len;
} license_data;

typedef struct {
    char name[32];
    uint32_t max_message_len;
} license_contents;

typedef struct {
    uint8_t signature[crypto_hash_BYTES]; //TODO: Wrong constant but happens to work :D
    uint8_t hash[crypto_hash_BYTES];
} program_signature;

#pragma pack(pop)

// Placeholder values
program_signature target_signature = {
    { 0xd3, 0x28, 0x20, 0x72, 0xc5, 0x6d, 0xed, 0x94, 0xad, 0x60, 0x4a, 0x0b, 0x31, 0xec, 0x39, 0x4c, 0x65, 0x7a, 0x27, 0x9c, 0xdd, 0x55, 0xed, 0x3e, 0x6d, 0x92, 0xa6, 0x0c, 0x69, 0x0b, 0x71, 0xdb, 0xb6, 0x73, 0x81, 0xc1, 0x86, 0x9b, 0x44, 0xa0, 0xcd, 0x19, 0x5b, 0x29, 0x3c, 0x09, 0x9d, 0x4d, 0xdd, 0x54, 0x5e, 0x88, 0x8f, 0x14, 0x38, 0x80, 0xbb, 0xe7, 0x15, 0x27, 0x5b, 0x0a, 0x23, 0x8d },
    { 0xa2, 0x28, 0x51, 0x80, 0x8e, 0x59, 0xf3, 0x2a, 0xb7, 0x09, 0x8b, 0x4d, 0xdb, 0x25, 0xf6, 0xbd, 0x4d, 0x7d, 0xbd, 0xfd, 0xa7, 0xd3, 0x5e, 0xc7, 0x92, 0xff, 0x24, 0xdc, 0x0f, 0xff, 0x78, 0xc0, 0x35, 0x91, 0xb5, 0x52, 0xe7, 0xc3, 0x0a, 0xec, 0x7f, 0x3b, 0x40, 0x17, 0x69, 0x22, 0xef, 0xdb, 0x57, 0xc2, 0x52, 0x65, 0x98, 0xd6, 0xbe, 0xb7, 0xd6, 0x31, 0xb7, 0x39, 0xca, 0x08, 0x6c, 0x7e }
};
uint8_t text_pubkey[crypto_sign_PUBLICKEYBYTES] = { 0xb8, 0x5c, 0x16, 0xc3, 0x5d, 0x1f, 0x43, 0x15, 0xf4, 0x67, 0x31, 0xe0, 0x5f, 0x89, 0x29, 0xa3, 0x1d, 0x60, 0x92, 0x32, 0xd6, 0xc7, 0xf9, 0xd3, 0xc8, 0xb0, 0xc9, 0x99, 0x2c, 0x21, 0xd9, 0xc7 };
uint8_t license_pubkey[crypto_sign_PUBLICKEYBYTES] = { 0x19, 0x56, 0x3f, 0x7a, 0xd6, 0xf5, 0x8b, 0xc6, 0xe7, 0x75, 0x2a, 0x90, 0xa4, 0x4a, 0x0d, 0x52, 0x0f, 0xd1, 0x6f, 0x0f, 0xfc, 0xfb, 0x87, 0x39, 0x03, 0x0b, 0x47, 0xcc, 0x94, 0xf9, 0x6c, 0xb8 };

uint8_t runtime_hash[crypto_hash_BYTES];


// Convert string of chars to its NULL-terminated representative string of hex
// numbers.  The returned pointer must be freed by the caller.
int bytes2hex(const uint8_t *data, const size_t data_len, char *hexstr, size_t hex_maxlen, const int capital)
{
    if(2*data_len+1 > hex_maxlen) { return 0; }

    const int a = capital ? 'A' - 1 : 'a' - 1;

    int i = 0;
    for (uint8_t c = data[0]; i < 2*data_len; c = data[i / 2])
    {
        hexstr[i++] = c > 0x9F ? (c / 16 - 9) | a : c / 16 | '0';
        hexstr[i++] = (c & 0xF) > 9 ? (c % 16 - 9) | a : c % 16 | '0';
    }
    hexstr[i] = '\0';

    return 1;
}

// Convert string of hex numbers to its equivalent char-stream
int hex2bytes(const char *hexstr, uint8_t *data, size_t data_maxlen, size_t *data_len)
{
    size_t data_len_internal = strlen(hexstr)/2;
    if(data_len_internal > data_maxlen) { return 0; }
    if(data_len != NULL) { *data_len = data_len_internal; }
    for (int i = 0, j = 0; i < data_len_internal; i++, j++)
    {
        data[i] = (hexstr[j] & '@' ? hexstr[j] + 9 : hexstr[j]) << 4, j++;
        data[i] |= (hexstr[j] & '@' ? hexstr[j] + 9 : hexstr[j]) & 0xF;
    }
    return 1;
}


void *find_image(void) {
    void* cur = (void*)(((uintptr_t)(&find_image)) & (~0xFFF));
    while(cur != NULL && *(uint32_t*)cur != ELF_MAGIC_BYTES) { cur -= 0x1000; }
    return cur;
}

int get_text_range(void *const base, void **text_start, uint64_t *text_len) {
    elf_header *elf_header = base;
    const uint16_t num_program_headers = elf_header->phnum;
    program_header *const program_header_table = base + elf_header->program_header_offset;
    for(uint16_t program_header_idx = 0; program_header_idx < num_program_headers; program_header_idx++) {
        program_header* program_header = &program_header_table[program_header_idx];
        if(program_header->flags == 5) { // if R_X, assume text segment
            *text_start = base + program_header->offset;
            *text_len = program_header->memsz;
            return 1;
        }
    }
    return 0;
}

void hash_text_segment(void) {
    void* base_ptr = find_image();
    void* text_start;
    uint64_t text_len;
    if(!get_text_range(base_ptr, &text_start, &text_len)) {
        printf("Failed to initialize ZetaProtec(tm), tampering detected, exiting.\n");
        exit(-1337);
    }
#ifdef DEBUG
    printf("Base: %p, Text: %p, Len: %lu\n", base_ptr, text_start, text_len);
#endif

    crypto_hash(runtime_hash, text_start, text_len);    
    
#ifdef DEBUG
    char text_hash_hex[2*crypto_hash_BYTES+1];
    bytes2hex(text_hash, crypto_hash_BYTES, text_hash_hex, 2*crypto_hash_BYTES+1, 0);
    printf("Self hash: %s\n", text_hash_hex);
#endif
}

int validate_license(license_contents *license) {
    FILE *license_file = fopen("license.dat", "r");
    license_data license_data;
    fread(&license_data, sizeof(license_data), 1, license_file);

#ifdef DEBUG
    char license_data_hex[2*sizeof(license_data)+1];
    bytes2hex((uint8_t*)&license_data, sizeof(license_data), license_data_hex, 2*sizeof(license_data)+1, 1);
    printf("Sig: %s\n", license_data_hex);
    printf("Name: %s\n", license_data.name);
    printf("Max message len: %u\n", license_data.max_message_len);
#endif

    uint8_t license_verified[sizeof(license_data)];

    unsigned long long license_len;
    //license_data.max_message_len = 11; // Try altering license
    int valid_sig = crypto_sign_open(license_verified, &license_len, (uint8_t*)&license_data, sizeof(license_data), license_pubkey);

    printf("License len: %llu, sig: %d\n", license_len, valid_sig);
    if(valid_sig != 0 || license_len != sizeof(license_contents)) {
        return 0;
    }

    memcpy(license, license_verified, sizeof(license_contents));

    return 1;
}

int validate_integrity(void) {
    uint8_t program_hash[sizeof(program_signature)];
    unsigned long long program_hash_len;

    int valid_sig = crypto_sign_open(program_hash, &program_hash_len, (uint8_t*)&target_signature, sizeof(program_signature), text_pubkey);
    printf("Hash len: %llu, sig: %d\n", program_hash_len, valid_sig);
    if(valid_sig != 0 || program_hash_len != crypto_hash_BYTES) {
        return 0;
    }

#ifdef DEBUG
    char signed_hash_hex[2*crypto_hash_BYTES+1];
    bytes2hex(target_signature.hash, crypto_hash_BYTES, signed_hash_hex, 2*crypto_hash_BYTES+1, 0);
    printf("Target hash: %s\n", signed_hash_hex);
    bytes2hex(runtime_hash, crypto_hash_BYTES, signed_hash_hex, 2*crypto_hash_BYTES+1, 0);
    printf("Runtime hash: %s\n", signed_hash_hex);
#endif

    if(0 != memcmp(target_signature.hash, runtime_hash, crypto_hash_BYTES)) {
        return 0;
    }

    return 1;
}

int main(int argc, char const *argv[], char const *envp[])
{
#ifdef DEBUG
    char* test_hex = "0011223344556677";
    uint8_t test_bytes[8];
    char test_hex2[16+1];
    if(!hex2bytes(test_hex, test_bytes, 8, NULL)) {
        printf("Failed to convert\n");
    }
    if(!bytes2hex(test_bytes, 8, test_hex2, 16+1, 1)) {
        printf("Failed to convert\n");
    }
    if(!memcmp(test_hex, test_hex2, 17)) {
        printf("Hex functions incorrect. Exiting!\n");
        return -1;
    }
#endif

    hash_text_segment();

    if(!validate_integrity()) {
        printf("Program has been tampered with, exiting.");
        exit(-1);
    }

    license_contents license;
    if(!validate_license(&license)) {
        printf("Invalid license. Exiting.");
        exit(-1);
    }

    // Check 1
    if( ((uint64_t*)target_signature.hash)[0] != ((uint64_t*)runtime_hash)[0] ) {
        __asm__("xor %rbx, %rbx");
    }

    printf("This version of ZetaCryptorPro is licensed to: %s\n", license.name);
    printf("You can encrypt message that are at most %u characters long.\n", license.max_message_len);

    printf("Please input the hex encoded key:\n");
    char line[1024];
    char *eof = fgets(line, sizeof(line), stdin);
    if(eof == NULL) {
        printf("Failed to read key\n");
        return -1;
    }

    // Check 2
    if( ((uint64_t*)target_signature.hash)[1] != ((uint64_t*)runtime_hash)[1] ) {
        __asm__("push %rax");
    }
    
    size_t line_len = strlen(line);
    if(line_len == 0) {
        printf("Empty message, exiting.\n");
        return -1;
    }

    // Check 3
    if( ((uint64_t*)target_signature.hash)[2] != ((uint64_t*)runtime_hash)[2] ) {
        __asm__("pop %rax");
    }

    line[line_len-1] = '\0';
    size_t keyhex_len = strlen(line);
    
    if(keyhex_len != 2*crypto_secretbox_KEYBYTES) {
        printf("Key must be exactly %u hex characters long, got %lu, exiting.\n", 2*crypto_secretbox_KEYBYTES, keyhex_len);
        return -1;
    }

    // Check 4
    if( ((uint64_t*)target_signature.hash)[3] != ((uint64_t*)runtime_hash)[3] ) {
        keyhex_len >>= 1;
    }

    unsigned char key[crypto_secretbox_KEYBYTES];
    hex2bytes(line, key, crypto_secretbox_KEYBYTES, NULL);

    // Check 5
    if( ((uint64_t*)target_signature.hash)[4] != ((uint64_t*)runtime_hash)[4] ) {
        key[0] = 0;
    }

    printf("Please input the message to encrypt:\n");
    eof = fgets(line, sizeof(line), stdin);
    if(eof == NULL) {
        printf("Failed to read message to encrypt\n");
        return -1;
    }
    
    // Check 6
    if( ((uint64_t*)target_signature.hash)[5] != ((uint64_t*)runtime_hash)[5] ) {
        line[0] = 0;
    }

    line_len = strlen(line);
    if(line_len == 0) {
        printf("Empty message, exiting.\n");
        return -1;
    }

    // Check 7
    if( ((uint64_t*)target_signature.hash)[6] != ((uint64_t*)runtime_hash)[6] ) {
        line_len >>= 1;
    }

    line[line_len-1] = '\0';
    size_t message_len = strlen(line);

    if(message_len > license.max_message_len) {
        printf("Sorry, your license only allows you to encrypt message that are at most %u characters long but you provided a message of %lu characters, exiting.\n", license.max_message_len, message_len);
        return -1;
    }

    size_t ciphertext_len = message_len + crypto_secretbox_BOXZEROBYTES + crypto_secretbox_MACBYTES;

    // Check 8
    if( ((uint64_t*)target_signature.hash)[7] != ((uint64_t*)runtime_hash)[7] ) {
        ciphertext_len = 0;
    }

    uint8_t *ciphertext = malloc(ciphertext_len);
    

    
    size_t plaintext_len = message_len + crypto_secretbox_ZEROBYTES;
    uint8_t *plaintext = malloc(plaintext_len);
    memset(plaintext, '\0', crypto_secretbox_ZEROBYTES);
    memcpy(plaintext + crypto_secretbox_ZEROBYTES, line, message_len);

    uint8_t nonce[crypto_secretbox_NONCEBYTES];
    randombytes(nonce, crypto_secretbox_NONCEBYTES);
    
    crypto_secretbox(ciphertext, plaintext, ciphertext_len, nonce, key);

    size_t output_len = ciphertext_len+crypto_secretbox_NONCEBYTES;
    char *ciphertext_hex = malloc(2*(output_len)+1);
    bytes2hex(nonce, crypto_secretbox_NONCEBYTES, ciphertext_hex, 2*crypto_secretbox_NONCEBYTES+1, 1);
    bytes2hex(ciphertext+crypto_secretbox_BOXZEROBYTES, message_len+crypto_secretbox_MACBYTES, ciphertext_hex+2*crypto_secretbox_NONCEBYTES, 2*(message_len+crypto_secretbox_MACBYTES)+1, 1);
    printf("Encryption: %s\n", ciphertext_hex);

    return 0;
}
