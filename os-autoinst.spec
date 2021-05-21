#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-autoinst
Version  : 8d4b96b9d9c4557a02ab36a481594c031f1973f7
Release  : 17
URL      : https://github.com/os-autoinst/os-autoinst/archive/8d4b96b9d9c4557a02ab36a481594c031f1973f7/os-autoinst-8d4b96b9d9c4557a02ab36a481594c031f1973f7.tar.gz
Source0  : https://github.com/os-autoinst/os-autoinst/archive/8d4b96b9d9c4557a02ab36a481594c031f1973f7/os-autoinst-8d4b96b9d9c4557a02ab36a481594c031f1973f7.tar.gz
Summary  : OS-level test automation
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: os-autoinst-bin = %{version}-%{release}
Requires: os-autoinst-data = %{version}-%{release}
Requires: os-autoinst-libexec = %{version}-%{release}
Requires: os-autoinst-license = %{version}-%{release}
Requires: os-autoinst-perl = %{version}-%{release}
Requires: os-autoinst-services = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cpan
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(opencv)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(theoraenc)
Patch1: 0001-Include-OpenCV-legacy-constants.patch
Patch2: 0002-Update-references-to-old-highgui.h.patch
Patch3: 0003-videoencoder-Use-CXXFLAGS-instead-of-CFLAGS.patch

%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer
and upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used
to test firefox and openoffice operation on top of a newly
installed OS.

%package bin
Summary: bin components for the os-autoinst package.
Group: Binaries
Requires: os-autoinst-data = %{version}-%{release}
Requires: os-autoinst-libexec = %{version}-%{release}
Requires: os-autoinst-license = %{version}-%{release}
Requires: os-autoinst-services = %{version}-%{release}

%description bin
bin components for the os-autoinst package.


%package data
Summary: data components for the os-autoinst package.
Group: Data

%description data
data components for the os-autoinst package.


%package doc
Summary: doc components for the os-autoinst package.
Group: Documentation

%description doc
doc components for the os-autoinst package.


%package libexec
Summary: libexec components for the os-autoinst package.
Group: Default
Requires: os-autoinst-license = %{version}-%{release}

%description libexec
libexec components for the os-autoinst package.


%package license
Summary: license components for the os-autoinst package.
Group: Default

%description license
license components for the os-autoinst package.


%package perl
Summary: perl components for the os-autoinst package.
Group: Default
Requires: os-autoinst = %{version}-%{release}

%description perl
perl components for the os-autoinst package.


%package services
Summary: services components for the os-autoinst package.
Group: Systemd services

%description services
services components for the os-autoinst package.


%prep
%setup -q -n os-autoinst-8d4b96b9d9c4557a02ab36a481594c031f1973f7
cd %{_builddir}/os-autoinst-8d4b96b9d9c4557a02ab36a481594c031f1973f7
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621640893
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1621640893
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-autoinst
cp %{_builddir}/os-autoinst-8d4b96b9d9c4557a02ab36a481594c031f1973f7/COPYING %{buildroot}/usr/share/package-licenses/os-autoinst/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install INSTALLDIRS=vendor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/debugviewer
/usr/bin/isotovideo
/usr/bin/snd2png

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/org.opensuse.os_autoinst.switch.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/os\-autoinst/*

%files libexec
%defattr(-,root,root,-)
/usr/libexec/os-autoinst/OpenQA/Benchmark/Stopwatch.pm
/usr/libexec/os-autoinst/OpenQA/Commands.pm
/usr/libexec/os-autoinst/OpenQA/Exceptions.pm
/usr/libexec/os-autoinst/OpenQA/Isotovideo/CommandHandler.pm
/usr/libexec/os-autoinst/OpenQA/Isotovideo/Interface.pm
/usr/libexec/os-autoinst/OpenQA/Isotovideo/NeedleDownloader.pm
/usr/libexec/os-autoinst/OpenQA/Isotovideo/Utils.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/BlockDev.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/BlockDevConf.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/ControllerConf.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/DriveController.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/DriveDevice.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/DrivePath.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/MutParams.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/PFlashDevice.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/Proc.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/Snapshot.pm
/usr/libexec/os-autoinst/OpenQA/Qemu/SnapshotConf.pm
/usr/libexec/os-autoinst/OpenQA/Test/RunArgs.pm
/usr/libexec/os-autoinst/autotest.pm
/usr/libexec/os-autoinst/backend/baseclass.pm
/usr/libexec/os-autoinst/backend/console_proxy.pm
/usr/libexec/os-autoinst/backend/driver.pm
/usr/libexec/os-autoinst/backend/generalhw.pm
/usr/libexec/os-autoinst/backend/ikvm.pm
/usr/libexec/os-autoinst/backend/ipmi.pm
/usr/libexec/os-autoinst/backend/pvm.pm
/usr/libexec/os-autoinst/backend/qemu.pm
/usr/libexec/os-autoinst/backend/s390x.pm
/usr/libexec/os-autoinst/backend/spvm.pm
/usr/libexec/os-autoinst/backend/svirt.pm
/usr/libexec/os-autoinst/backend/virt.pm
/usr/libexec/os-autoinst/basetest.pm
/usr/libexec/os-autoinst/bmwqemu.pm
/usr/libexec/os-autoinst/commands.pm
/usr/libexec/os-autoinst/consoles/VNC.pm
/usr/libexec/os-autoinst/consoles/console.pm
/usr/libexec/os-autoinst/consoles/icewm.cfg
/usr/libexec/os-autoinst/consoles/ipmiSol.pm
/usr/libexec/os-autoinst/consoles/localXvnc.pm
/usr/libexec/os-autoinst/consoles/network_console.pm
/usr/libexec/os-autoinst/consoles/remoteVnc.pm
/usr/libexec/os-autoinst/consoles/s3270.pm
/usr/libexec/os-autoinst/consoles/serial_screen.pm
/usr/libexec/os-autoinst/consoles/sshIucvconn.pm
/usr/libexec/os-autoinst/consoles/sshVirtsh.pm
/usr/libexec/os-autoinst/consoles/sshVirtshSUT.pm
/usr/libexec/os-autoinst/consoles/sshX3270.pm
/usr/libexec/os-autoinst/consoles/sshXtermIPMI.pm
/usr/libexec/os-autoinst/consoles/sshXtermVt.pm
/usr/libexec/os-autoinst/consoles/ssh_screen.pm
/usr/libexec/os-autoinst/consoles/ttyConsole.pm
/usr/libexec/os-autoinst/consoles/virtio_terminal.pm
/usr/libexec/os-autoinst/consoles/vnc_base.pm
/usr/libexec/os-autoinst/crop.py
/usr/libexec/os-autoinst/cv.pm
/usr/libexec/os-autoinst/distribution.pm
/usr/libexec/os-autoinst/dmidata/dell_e6330/smbios_type_1.bin
/usr/libexec/os-autoinst/dmidata/dell_e6330/smbios_type_2.bin
/usr/libexec/os-autoinst/dmidata/dell_e6330/smbios_type_3.bin
/usr/libexec/os-autoinst/dmidata/dump
/usr/libexec/os-autoinst/lockapi.pm
/usr/libexec/os-autoinst/mmapi.pm
/usr/libexec/os-autoinst/myjsonrpc.pm
/usr/libexec/os-autoinst/needle.pm
/usr/libexec/os-autoinst/ocr.pm
/usr/libexec/os-autoinst/os-autoinst-openvswitch
/usr/libexec/os-autoinst/osutils.pm
/usr/libexec/os-autoinst/testapi.pm
/usr/libexec/os-autoinst/tools/absolutize
/usr/libexec/os-autoinst/tools/check_coverage
/usr/libexec/os-autoinst/tools/lib/perlcritic/Perl/Critic/Policy/ConsistentQuoteLikeWords.pm
/usr/libexec/os-autoinst/tools/lib/perlcritic/Perl/Critic/Policy/HashKeyQuotes.pm
/usr/libexec/os-autoinst/tools/preparepool
/usr/libexec/os-autoinst/tools/tidy
/usr/libexec/os-autoinst/videoencoder

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-autoinst/4cc77b90af91e615a64ae04893fdffa7939db84c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/tinycv/.packlist
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/tinycv/tinycv.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/tinycv.pm

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/os-autoinst-openvswitch.service
