## Example usage

Include whole file

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!" << std::endl;
    return 0;
}
```

Include just lines 20-28 from file

```cpp
endian get_system_endian() {
    aliasing test;
    test.packed = 1;
    if (test.bytes.byte_4 > 0) {
        return endian::big;
    } else {
        return endian::small;
    }
}

```
