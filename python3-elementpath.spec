#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	XPath 1.0/2.0 parsers and selectors for ElementTree and lxml
Summary(pl.UTF-8):	Parsery i selektory XPath 1.0/2.0 dla ElementTree oraz lxml
Name:		python3-elementpath
Version:	2.5.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/elementpath/
Source0:	https://files.pythonhosted.org/packages/source/e/elementpath/elementpath-%{version}.tar.gz
# Source0-md5:	352e7980c3be9716a355f7588bd151c2
URL:		https://pypi.org/project/elementpath/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-lxml
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
The proposal of this package is to provide XPath 1.0 and 2.0 selectors
for Python's ElementTree XML data structures, both for the standard
ElementTree library and for the lxml.etree library.

%description -l pl.UTF-8
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

%build
%py3_build

%if %{with tests}
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
