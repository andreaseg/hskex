#ifndef LONG_FILE_H
#define LONG_FILE_H

union aliasing {
    struct bytes {
        char byte_1;
        char byte_2;
        char byte_3;
        char byte_4;
    };
    bytes bytes;
    unsigned long long int packed;
};

enum endian {
    big,
    small
};

endian get_system_endian() {
    aliasing test;
    test.packed = 1;
    if (test.bytes.byte_4 > 0) {
        return endian::big;
    } else {
        return endian::small;
    }
}


#endif