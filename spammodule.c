#include "python.h" 

struct Albat {
	char alphabat;
	int count;
};

static PyObject * 

//spam_strlen(PyObject *self, PyObject *args)
//{
//	const char* str, scnt = NULL;
//	int len;
////	char alphaBat[] = { "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" };
//
//    if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
//         return NULL; 
//
//    len = strlen(str); 
//
//
//	return  Py_BuildValue("i", len);
//}

spam_strlen(PyObject *self, PyObject *args)
{
	const char* str = NULL;
	char* str1;
	int len;
	//	char alphaBat[] = { "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" };

	if (!PyArg_ParseTuple(args, "s", &str)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;

	len = strlen(str);

	str1 = (char*)malloc(sizeof(char)*len);

	for (int i = 0; i < len; ++i) {
		str1[len - i] = str[i];
	}
	const char* kk = str1;

	return  Py_BuildValue("s", kk);
}

static PyMethodDef SpamMethods[] = {
{"strlen", spam_strlen, METH_VARARGS,
 "count a string length."},
 {NULL, NULL, 0, NULL} // 배열의 끝을 나타냅니다.
}; 

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // 모듈 이름
    "It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
