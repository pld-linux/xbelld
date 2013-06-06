Summary:	X bell replacement
Summary(pl.UTF-8):	Zamiennik dzwonka systemowego pod X
Name:		xbelld
Version:	0.3.4
Release:	1
License:	GPL v3
Group:		X11/Applications
#Source0-Download: https://code.google.com/p/xbelld/downloads/list
Source0:	http://xbelld.googlecode.com/files/%{name}-%{version}.tbz2
# Source0-md5:	97bdba8c9c306af51e1abf228df3d9b9
URL:		http://code.google.com/p/xbelld/
BuildRequires:	alsa-lib-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny utility to aid people who either don't like the default PC
speaker beep, or use an ALSA driver that doesn't yet have support for
the PC speaker (e.g. the AD1981 chipset in the snd_hda_intel driver).

xbelld performs a given action every time the X bell is rung. The
actions xbelld can currently perform include running a specified
program, emulating the PC speaker beep using your sound card
(default), or playing a PCM encoded WAVE file.

xbelld can also throttle the bell if it is rung too often (e.g. some
terminal program goes crazy), and/or disable the audible bell (so
that you don't get the annoying PC speaker beep in addition to your
xbelld action).

%description -l pl.UTF-8
Małe narzędzie dla ludzi, którzy nie mają PC speakera, bądź używają
sterownika dźwięku, który nie obsługuje go (np. układ AD1981 w
sterowniku snd_hda_intel).

xbelld wykonuje podaną akcję za każdym razem, gdy odzywa się dzwonek
pod X. Możliwe akcje obejmują uruchomienie określonego programu,
emulacja PC speakera za pomocą karty dźwiękowej (domyślnie), lub
odtworzenie pliku PCM w formacie WAVE.

xbelld potrafi również stłumić dźwięk, jeśli jest wywoływany zbyt
często (np. gdy utraci się kontrolę nad jakimś programem
terminalowym), lub wyłączyć dźwięk (aby nie słyszeć denerwującego
sygnału równocześnie ze zdefiniowaną akcją).

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DVERSION="\\\"%{version}\\\"" -DHAVE_ALSA" \
	LDFLAGS="%{rpmldflags} -lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xbelld $RPM_BUILD_ROOT%{_bindir}
install xbelld.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/xbelld
%{_mandir}/man1/xbelld.1*
