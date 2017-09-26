Name: aisdecoder
Summary: Decode AIS signals
Version: 1.0.0
Release: 0.1%{?dist}
License: GPLv3+
Source: http://www.aishub.net/downloads/aisdecoder-1.0.0.tar.gz

BuildRequires: cmake
BuildRequires: pulseaudio-libs-devel
BuildRequires: alsa-lib-devel

%description
AISDecoder streams AIS sentences via UDP and it is quite easy to
integrate it with AISDispatcher or other AIS software which listens
for incoming UDP AIS data.

http://www.aishub.net/ais-decoder

%prep
%setup0
mkdir build

%build
cd build
%cmake ..
%make_build

%install
cd build
mkdir -p %{buildroot}%{_bindir}
cp -a aisdecoder %{buildroot}%{_bindir}

%files
%{_bindir}/aisdecoder
