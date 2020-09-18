#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	XPath 1.0/2.0 parsers and selectors for ElementTree and lxml
Summary(pl.UTF-8):	Parsery i selektory XPath 1.0/2.0 dla ElementTree oraz lxml
Name:		python-elementpath
Version:	1.3.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/elementpath/
Source0:	https://files.pythonhosted.org/packages/source/e/elementpath/elementpath-%{version}.tar.gz
# Source0-md5:	3712104ae5970878a112c31aea71a503
Patch0:		%{name}-hash.patch
URL:		https://pypi.org/project/elementpath/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-lxml
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-lxml
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The proposal of this package is to provide XPath 1.0 and 2.0 selectors
for Python's ElementTree XML data structures, both for the standard
ElementTree library and for the lxml.etree library.

%description -l pl.UTF-8
Celem tego pakietu jest udostępnienie selektorów XPath 1.0 i 2.0 do
pythonowych struktur danych XML ElementTree, zarówno dla ElementTree z
biblioteki strandardowej, jak i lxml.etree.

%package -n python3-elementpath
Summary:	XPath 1.0/2.0 parsers and selectors for ElementTree and lxml
Summary(pl.UTF-8):	Parsery i selektory XPath 1.0/2.0 dla ElementTree oraz lxml
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-elementpath
The proposal of this package is to provide XPath 1.0 and 2.0 selectors
for Python's ElementTree XML data structures, both for the standard
ElementTree library and for the lxml.etree library.

%description -n python3-elementpath -l pl.UTF-8
Celem tego pakietu jest udostępnienie selektorów XPath 1.0 i 2.0 do
pythonowych struktur danych XML ElementTree, zarówno dla ElementTree z
biblioteki strandardowej, jak i lxml.etree.

%package apidocs
Summary:	API documentation for Python elementpath module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona elementpath
Group:		Documentation

%description apidocs
API documentation for Python elementpath module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona elementpath.

%prep
%setup -q -n elementpath-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} tests/test_elementpath.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest
%endif
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/elementpath
%{py_sitescriptdir}/elementpath-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-elementpath
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/elementpath
%{py3_sitescriptdir}/elementpath-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
