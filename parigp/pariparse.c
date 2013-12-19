#include<Python.h>
#include<pari/pari.h>

static PyObject * pariparse_run(PyObject *self, PyObject *args) {
    pari_init(40000000, 2);
    const char *pari_code;
    char *outstr;

    if (!PyArg_ParseTuple(args, "s", &pari_code)) { return NULL; }
    outstr = GENtostr(gp_read_str(pari_code));
    pari_close();
    return Py_BuildValue("s", outstr);
}

static PyMethodDef PariparseMethods[] = {
    {"run", pariparse_run, METH_VARARGS, "Run a pari command."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initpariparse(void) {
    (void) Py_InitModule("pariparse", PariparseMethods);
}