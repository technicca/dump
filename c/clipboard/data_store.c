// data_store.c
#include "data_store.h"
#include <string.h>

char store[MAX_SLOTS][MAX_DATA_SIZE];

void init_store(){
    for(int i = 0; i < MAX_SLOTS; i++){
        store[i][0] = '\0';
    }
}

void save_data(int slot, char* data){
    strncpy(store[slot], data, MAX_DATA_SIZE);
}

char* get_data(int slot){
    return store[slot];
}
