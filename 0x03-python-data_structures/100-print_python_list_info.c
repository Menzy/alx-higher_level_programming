#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    // Get the size of the Python list
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    // Get the allocated space for the list
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    // Iterate through each element in the list
    for (i = 0; i < size; i++)
    {
        // Get the i-th item from the list
        item = PyList_GetItem(p, i);

        // Print the index and the type name of each element
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
