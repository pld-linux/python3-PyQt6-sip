%define		module	PyQt6-sip
Summary:	The sip module support for PyQt6
Name:		python3-%{module}
Version:	13.9.1
Release:	1
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/MODULE/
Source0:	https://files.pythonhosted.org/packages/source/p/pyqt6_sip/pyqt6_sip-%{version}.tar.gz
# Source0-md5:	43f2c56293c48b4fbc62021844e017b6
URL:		https://www.riverbankcomputing.com/software/sip/
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sip extension module provides support for the PyQt6 package.

%prep
%setup -q -n pyqt6_sip-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py3_sitedir}/PyQt6/*.so
%{py3_sitedir}/PyQt6_sip-%{version}-py*.egg-info
