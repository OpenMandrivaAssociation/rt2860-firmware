%define rtname RT2860_Firmware

Summary:	Firmware for the RT2860 chip
Name:		rt2860-firmware
Version:	11
Release:	5
# http://www.ralinktech.com.tw/data/drivers/%{rtname}_V%{version}.zip
# (Repackaged as tar.bz2 because of unzip warnings that makes build fail)
Source0:	%{rtname}_V%{version}.tar.bz2
License:	Redistributable, no modification permitted
Group:		System/Kernel and hardware
Url:		http://www.ralinktech.com
BuildArch:	noarch

%description
This package contains the firmware files for the RT2860 chip.

%prep
%setup -q -n %{rtname}_V%{version}

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 rt*.bin %{buildroot}/lib/firmware

%files
%doc LICENSE.ralink-firmware.txt
/lib/firmware/rt*.bin
