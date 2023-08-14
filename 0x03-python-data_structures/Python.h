#ifndef PYTHON_H_INCLUDED
#define PYTHON_H_INCLUDED

#include <Python.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p);

#ifdef __cplusplus
}
#endif

#endif /* PYTHON_H_INCLUDED */

