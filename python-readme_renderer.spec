Name:		python-readme_renderer
Version:	44.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/readme-renderer/readme_renderer-%{version}.tar.gz
Summary:	readme_renderer is a library for rendering readme descriptions for Warehouse
URL:		https://pypi.org/project/readme-renderer/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
Requires:	python-nh3
BuildSystem:	python
BuildArch:	noarch

%description
readme_renderer is a library for rendering readme descriptions for Warehouse

%files
%{py_sitedir}/readme_renderer
%{py_sitedir}/readme_renderer-*.*-info
