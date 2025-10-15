def pip_import(module_name, pip_install_names=None, *, package=None):
    import importlib

    try:
        m = importlib.import_module(module_name, package=package)
    except ImportError:
        import pip

        pip.main(["install", *(pip_install_names or [module_name])])
        m = importlib.import_module(module_name, package=package)

    return m


__all__ = ["pip_import"]
