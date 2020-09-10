#include <Python.h>

/**
 * print_python_list_info - prints info of a list object of Python
 * @p: pointer of the Python list object
 *
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int list_size = (int)PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", (int)(((PyListObject *)p)->allocated));
	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: %s\n", i
		       , Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
