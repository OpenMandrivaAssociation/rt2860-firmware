%define name rt2860-firmware
%define rtname RT2860_Firmware
%define version 11
%define release %mkrel 2

Summary: Firmware for the RT2860 chip
Name: %{name}
Version: %{version}
Release: %{release}
# http://www.ralinktech.com.tw/data/drivers/%{rtname}_V%{version}.zip
# (Repackaged as tar.bz2 because of unzip warnings that makes build fail)
Source: %{rtname}_V%{version}.tar.bz2
License: Redistributable, no modification permitted
Group: System/Kernel and hardware
Url: http://www.ralinktech.com
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
This package contains the firmware files for the RT2860 chip.

%prep
%setup -q -n %{rtname}_V%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/firmware
install -m644 rt*.bin %{buildroot}/lib/firmware

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE.ralink-firmware.txt
/lib/firmware/rt*.bin
