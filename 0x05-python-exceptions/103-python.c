#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
long unsigned int size;
unsigned int n;
char *test_str = NULL;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
test_str = ((PyBytesObject *)p)->ob_sval;
printf("  size: %lu\n", size);
printf("  trying string: %s\n", test_str);
if (size < 10)
{
printf("  first %lu bytes:", size + 1);
}
else
{
printf("  first 10 bytes:");
}
for (n = 0; n <= size && n < 10; n++)
{
printf(" %02hhx", test_str[n]);
}
printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
PyFloatObject *float_obj = (PyFloatObject *)p;
double num = float_obj->ob_fval;
char *str = NULL;

printf("[.] float object info\n");
if (!PyFloat_Check(float_obj))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
str = PyOS_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", str);  
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
long unsigned int size;
unsigned int n;
PyListObject *list = (PyListObject *)p;
const char *type;

printf("[*] Python list info\n");
if (!PyList_Check(list))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
printf("[*] Size of the Python List = %lu\n", size);
printf("[*] Allocated = %lu\n", list->allocated);
for (n = 0; n < size; n++)
{
type = (list->ob_item[n])->ob_type->tp_name;
printf("Element %i: %s\n", n, type);
if (!strcmp(type, "bytes"))
{
print_python_bytes(list->ob_item[n]);
}
if (!strcmp(type, "float"))
{
print_python_float(list->ob_item[n]);
}
}
}
