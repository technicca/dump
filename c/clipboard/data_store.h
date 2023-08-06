// data_store.h

#define MAX_SLOTS 9
#define MAX_DATA_SIZE 1024

void init_store();
void save_data(int slot, char* data);
char* get_data(int slot);
