
Summary:	Compact In-System Programmer
Name:		cisp
Version:	1.0.4
Release:	0.1
License:	GPL
URL:		http://www.funet.fi/pub/cbm/crossplatform/transfer/C2N232/
Group:		Development/Tools
Source0:	http://www.funet.fi/pub/cbm/crossplatform/transfer/C2N232/firmware/%{name}-%{version}.tar.gz
# Source0-md5:	60ec135286b551a4ea27c5d5e7d6b90f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CISP is a special compact In-System Programmer for the C2N232 project
by Marko Mäkelä. CISP transfers data to and from the non-volatile
program or data memory of an Atmel AVR RISC processor over the Serial
Peripheral Interface (SPI).

Nevertheless you could use this programmer software together with
following hardware components:

    - c2n232 serial (RESET=DTR SCK=RTS MOSI=TXD MISO=CTS)
    - dasa serial (RESET=RTS SCK=DTR MOSI=TXD MISO=CTS)
    - ponyprog serial (RESET=TXD SCK=RTS MOSI=DTR MISO=CTS)
    - dapa parallel (RESET=INIT SCK=STROBE MOSI=D0 MISO=BUSY)
    - dt006 parallel (RESET=D2 SCK=D3 MOSI=D0 MISO=BUSY)
    - stk200 Atmel STK200 Evaluation Board (parallel)

%prep
%setup -q

%build
%{__make} -f Makefile.unixpc		\
	CFLAGS="%{rpmcflags}"		\
	CXXFLAGS="%{rpmcflags}"		\
	CC="%{__cc}"			\
	CXX="%{__cxx}"			\
	PREFIX=%{_prefix}		\
	BINDIR=%{_bindir}		\
	MANDIR=%{_mandir}/man1	\
	all cisp.dvi

%install
rm -rf $RPM_BUILD_ROOT
%{__make}	-f Makefile.unixpc				\
	PREFIX=$RPM_BUILD_ROOT%{_prefix}			\
	BINDIR=$RPM_BUILD_ROOT%{_bindir}		\
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1	\
	install installman

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
