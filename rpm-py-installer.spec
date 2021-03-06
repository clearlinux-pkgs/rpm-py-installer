#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rpm-py-installer
Version  : 1.1.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/21/37/f557c91ec825ebf4aa1fd0603359c106e70d4b6443a31e5d98f618340178/rpm-py-installer-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/37/f557c91ec825ebf4aa1fd0603359c106e70d4b6443a31e5d98f618340178/rpm-py-installer-1.1.0.tar.gz
Summary  : RPM Python binding Installer
Group    : Development/Tools
License  : MIT
Requires: rpm-py-installer-bin = %{version}-%{release}
Requires: rpm-py-installer-license = %{version}-%{release}
Requires: rpm-py-installer-python = %{version}-%{release}
Requires: rpm-py-installer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
An installer to enable the RPM Python binding in any environment.
        See "Homepage" on GitHub for detail.

%package bin
Summary: bin components for the rpm-py-installer package.
Group: Binaries
Requires: rpm-py-installer-license = %{version}-%{release}

%description bin
bin components for the rpm-py-installer package.


%package license
Summary: license components for the rpm-py-installer package.
Group: Default

%description license
license components for the rpm-py-installer package.


%package python
Summary: python components for the rpm-py-installer package.
Group: Default
Requires: rpm-py-installer-python3 = %{version}-%{release}

%description python
python components for the rpm-py-installer package.


%package python3
Summary: python3 components for the rpm-py-installer package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rpm-py-installer package.


%prep
%setup -q -n rpm-py-installer-1.1.0
cd %{_builddir}/rpm-py-installer-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629942703
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rpm-py-installer
cp %{_builddir}/rpm-py-installer-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/rpm-py-installer/56f55d6d6651181134722362475574c0a0963dd1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/install.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rpm-py-installer/56f55d6d6651181134722362475574c0a0963dd1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
