#include "/usr/include/openssl/sha.h"
#include "hmac.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char * argv[]){

	// 1. Obtención de clave 'key' y mensaje 'message'

	// Lectura de clave y mensaje a partir de parámetros
	char * k = malloc(strlen(argv[1]));
	strcpy(k, argv[1]);
	char * m = malloc(strlen(argv[2]));
	strcpy(m, argv[2]);

	// Obtención de largo de clave y mensaje
	int key_length=strlen(k) ;
	int message_length=strlen(m) ;

	// Pasaje de arreglo dinámico a estático (por facilidad de operación)
	unsigned char key[key_length];
	unsigned char message[message_length];
	memcpy(key, k, key_length);
	memcpy(message, m, message_length);
	free(k);
	free(m);

	// 2. Obtención de parámetros base

	// Procesamiento de la clave 'key' según su largo
	unsigned char * processed_key = malloc(SHA1_BLOCK_LENGTH);

	// Concatenar 0x00 si el largo de clave es menor al de bloque
	if(key_length < SHA1_BLOCK_LENGTH){
		for(int i=0; i < key_length; i++){
			processed_key[i] = key[i];
		}
		for(int i = key_length; i < SHA1_BLOCK_LENGTH; i++){
			 processed_key[i] = 0x00;
		}
	}
	// Hashear y concatenar 0x00 si el largo de clave es mayor al de bloque
	else if(key_length > SHA1_BLOCK_LENGTH){
		unsigned char hash_key[SHA_DIGEST_LENGTH];
		SHA1(key, key_length, hash_key);
		for(int i=0;i<SHA1_OUTPUT_LENGTH;i++){
			processed_key[i] = hash_key[i];
		}
		for(int i=0; i < SHA1_BLOCK_LENGTH - SHA1_OUTPUT_LENGTH; i++){
			processed_key[i + SHA1_OUTPUT_LENGTH] = 0x00;
		}
	}
	else {
		for(int i=0; i < SHA1_BLOCK_LENGTH; i++){
			processed_key[i] = key[i];
		}
	}


	// Cálculo de claves utilizando IPAD y OPAD
	unsigned char k_opad[SHA1_BLOCK_LENGTH];
	unsigned char k_ipad[SHA1_BLOCK_LENGTH];
	for(int i=0; i < SHA1_BLOCK_LENGTH; i++){
		k_opad[i] = processed_key[i] ^ OPAD;
		k_ipad[i] = processed_key[i] ^ IPAD;
	}


	// 3. Cálculo del código HMAC

	// Concatenación de k_ipad y mensaje
	unsigned char h1[SHA1_OUTPUT_LENGTH];
	unsigned char iv1[SHA1_BLOCK_LENGTH + message_length];
	for(int i=0; i< SHA1_BLOCK_LENGTH; i++){
		iv1[i] = k_ipad[i];
	}
	for(int i=0; i< message_length; i++){
		iv1[i + SHA1_BLOCK_LENGTH] = message[i];
	}

	// Cálculo del primer hash -> h1 = H(K ^ ipad|| m)
	SHA1(iv1, SHA1_BLOCK_LENGTH + message_length, h1);

	// Concatenación de k_opad y h1
	unsigned char h2[SHA1_OUTPUT_LENGTH];
	unsigned char iv2[SHA1_OUTPUT_LENGTH + SHA1_BLOCK_LENGTH];
	for(int i=0; i< SHA1_BLOCK_LENGTH; i++){
		iv2[i] = k_opad[i];
	}
	for(int i=0; i< SHA1_OUTPUT_LENGTH; i++){
		iv2[i + SHA1_BLOCK_LENGTH] = h1[i];
	}

	// Cálculo del segundo hash -> h2 = H(K ^ opad|| h1)
	SHA1(iv2, SHA1_OUTPUT_LENGTH+SHA1_BLOCK_LENGTH , h2);
	

	// Liberación de memoria e impresión del hash generado
	free(processed_key);
	for(int i = 0; i < 20; i++) printf("%02x", h2[i]);
		printf("\n");

	return 1;
}
