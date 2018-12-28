#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : discover
Version  : 0.4.0
Release  : 22
URL      : http://pypi.debian.net/discover/discover-0.4.0.tar.gz
Source0  : http://pypi.debian.net/discover/discover-0.4.0.tar.gz
Summary  : Test discovery for unittest. Backported from Python 2.7 for Python 2.4+
Group    : Development/Tools
License  : BSD-3-Clause
Requires: discover-bin
Requires: discover-python3
Requires: discover-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
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
Requires: discover-python3

%description python
python components for the discover package.


%package python3
Summary: python3 components for the discover package.
Group: Default
Requires: python3-core

%description python3
python3 components for the discover package.


%prep
%setup -q -n discover-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532217360
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/discover

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
