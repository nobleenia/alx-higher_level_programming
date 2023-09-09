#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic information about a Python list
 * @p: pointer to a Python list (PyObject *)
 */
void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int i;
PyListObject *obj = (PyListObject *)p;

printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", obj->allocated);

for (i = 0; i < size; i++)
{
printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
}
