#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	XPath 1.0/2.0/3.0 parsers and selectors for ElementTree and lxml
Summary(pl.UTF-8):	Parsery i selektory XPath 1.0/2.0/3.0 dla ElementTree oraz lxml
# beware of python3-xmlschema compatibility (xmlschema 2.1.x requires elementpath 3.x)
Name:		python3-elementpath
Version:	3.0.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/elementpath/
Source0:	https://files.pythonhosted.org/packages/source/e/elementpath/elementpath-%{version}.tar.gz
# Source0-md5:	c4b193e1eb5148bdb493944036fdff20
URL:		https://pypi.org/project/elementpath/
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-lxml
#BuildRequires:	python3-xmlschema >= 2.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The proposal of this package is to provide XPath 1.0, 2.0 and 3.0
selectors for Python's ElementTree XML data structures, both for the
standard ElementTree library and for the lxml.etree library.

%description -l pl.UTF-8
Celem tego pakietu jest udostępnienie selektorów XPath 1.0, 2.0 i 3.0
do pythonowych struktur danych XML ElementTree, zarówno dla
ElementTree z biblioteki strandardowej, jak i lxml.etree.

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

%build
%py3_build

%if %{with tests}
LC_ALL=C.UTF-8 \
%{__python3} -m unittest
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/elementpath
%{py3_sitescriptdir}/elementpath-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
