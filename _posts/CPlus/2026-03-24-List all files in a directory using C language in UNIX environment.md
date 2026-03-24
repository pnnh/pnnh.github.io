---
layout: post
title: "List all files in a directory using C language in UNIX environment"
date: 2026-03-24 00:00:00 +0800
categories: [CPlus]
tags: [cpp, cmake]
---

Demonstrate listing all files in a directory using C language in a UNIX environment

### Test Environment

Tested successfully on Ubuntu 24.04. It should work in other UNIX-like environments as well. Windows is theoretically not supported.

### Source Code Snippet

```c
#include <stdio.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
  printf("hello %s\n", "world");

  DIR *dp;
  struct dirent *dirp;

  if (argc != 2) {
    return 1;
  }

  if ((dp = opendir(argv[1])) == NULL) {
    fprintf(stderr, "can't open %s", argv[1]);
    return 2;
  }

  while((dirp = readdir(dp)) != NULL) {
    printf("%s\n", dirp->d_name);
  }

  closedir(dp);
  return 0;
}
```

Complete source code address: [pnnh/apue-listfile](https://github.com/pnnh/apue-listfile.git)

### Source Code Explanation

Calling ```opendir``` returns a ```DIR*```, which is an opaque pointer to a specific directory. Subsequent directory operation functions require this pointer to be passed.

Calling ```readdir``` returns a ```dirent*```, which points to an entry in the directory, possibly a file or folder, containing the file name.

After directory operations are complete, ```closedir``` must be called to close the directory to prevent resource leaks.

### Compilation

Enter the source code directory and execute the following commands:

```bash
mkdir cmake-build && cd cmake-build
cmake ..
make
```

An executable file named ```ApueListfile``` will be generated in the build directory.

If a compilation error occurs, please repeat the above compilation steps based on the error message.

### Execution
Run the program using the command ```./ApueListfile <directory>```

Here, ```<directory>``` must be an absolute directory path. For example, the following commands will execute successfully:

```bash
./ApueListfile /tmp
./ApueListfile /home
./ApueListfile /var
```

**Note:** The current user must have access permissions to the specified directory.
