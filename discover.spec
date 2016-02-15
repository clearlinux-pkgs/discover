#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : discover
Version  : 0.4.0
Release  : 10
URL      : https://pypi.python.org/packages/source/d/discover/discover-0.4.0.tar.gz
Source0  : https://pypi.python.org/packages/source/d/discover/discover-0.4.0.tar.gz
Summary  : Test discovery for unittest. Backported from Python 2.7 for Python 2.4+
Group    : Development/Tools
License  : BSD-3-Clause
Requires: discover-bin
Requires: discover-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This is the test discovery mechanism and ``load_tests`` protocol for unittest
backported from Python 2.7 to work with Python 2.4 or more recent (including
Python 3).

%package bin
Summary: bin components for the discover package.
Group: Binaries

%description bin
bin components for the discover package.


%package python
Summary: python components for the discover package.
Group: Default

%description python
python components for the discover package.


%prep
%setup -q -n discover-0.4.0

%build
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
%{__python} setup.py test
%install
rm -rf %{buildroot}
python3 setup.py install --root=%{buildroot}
python3 setup.py clean
python setup.py build
python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/discover

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
