def pip_import(module_name, from_=None, package_names=None):
    import importlib

    try:
        return importlib.import_module(module_name, package=from_)
    except ImportError:
        import pip

        pip.main(["install", *(package_names or [module_name])])
        return importlib.import_module(module_name, package=from_)


__all__ = ["pip_import"]
