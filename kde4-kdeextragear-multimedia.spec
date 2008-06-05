%define		orgname kdeextragear-multimedia
%define		snap 816494
Summary:	extra multimedia
Summary(pl.UTF-8):	Dodatkowe programy multimedialne
Name:		kde4-kdeextragear-multimedia
Version:	4.0.81
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/%{orgname}-%{snap}.tar.bz2
# Source0-md5:	bd11404c11be3fc164944843295fb25b
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	kde4-kdemultimedia-devel
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
extra multimedia.

%description -l pl.UTF-8
Dodatkowe programy multimedialne.

%package -n kde4-amarok
Summary:	A KDE audio player
Summary(pl.UTF-8):	Odtwarzacz audio dla KDE
Group:		X11/Applications/Multimedia

%description -n kde4-amarok
A KDE audio player.

%description -n kde4-amarok -l pl.UTF-8
Odtwarzacz audio dla KDE.

%package -n kde4-k3b
Summary:	The CD Kreator
Summary(pl.UTF-8):	Kreator CD
Group:		X11/Applications

%description -n kde4-k3b
The CD Kreator features:
 - the most userfriendly interface ever ;-)
 - writing audio-CDs
 - writing ISO-CDs
 - writing existing iso-images to CD
 - CD copy (data, audio, mixed mode)
 - blanking of CD-RWs
 - CD ripping to WAV
 - dvd ripping with the transcode tools
 - DivX/XviD encoding
 - K3b checks if the user inserted an empty disk
 - Retrieving CD info and toc
 - Support for ATAPI drives without SCSI-emulation for reading
 - integrated full featured audio player 

%description -n kde4-k3b -l pl.UTF-8
Własności Kreatora CD:
 - najbardziej przyjazny dla użytkownika interfejs ;-)
 - zapisywanie płyt CD-Audio
 - zapisywanie płyt ISO
 - zapisywanie istniejących obrazów ISO na CD
 - kopiowanie CD (data/audio/mixed - z danymi, dźwiękiem i mieszane)
 - czyszczenie płyt CD-RW
 - rippowanie CD do plików WAV
 - rippowanie DVD przy użyciu narzędzi transcode
 - kodowanie DivX/XviD
 - sprawdzanie, czy użytkownik włożył czystą płytę
 - odtwarzania CD-info i TOC
 - obsługa nagrywarek ATAPI bez emulacji SCSI przy odczycie
 - zintegrowany odtwarzacz płyt audio o pełnych możliwościach

%prep
%setup -q -n %{orgname}-%{snap}

%build
install -d {amarok/build, k3b/build}
cd amarok/build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

cd ../k3b/build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C amarok/build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%{__make} -C k3b/build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

#%find_lang amarok --with-kde
#%find_lang k3b	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde4-amarok
%defattr(644,root,root,755)

%files -n kde4-k3b
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/k3b
%attr(755,root,root) %{_bindir}/k3bsetup
%{_includedir}/*.h
%{_libdir}/kde4/k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bffmpegdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bflacdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3blibsndfiledecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bmaddecoder.so
%{_libdir}/kde4/k3bmpcdecoder.desktop
%attr(755,root,root) %{_libdir}/kde4/k3bmpcdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bsoxencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bwavedecoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bsetup2.so
%attr(755,root,root) %{_libdir}/kde4/kio_videodvd.so
%attr(755,root,root) %{_libdir}/libk3b.so
%attr(755,root,root) %{_libdir}/libk3b.so.4
%attr(755,root,root) %{_libdir}/libk3b.so.4.0.0
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%attr(755,root,root) %{_libdir}/libk3bdevice.so.6
%attr(755,root,root) %{_libdir}/libk3bdevice.so.6.0.0
%{_desktopdir}/kde4/k3b.desktop
%{_datadir}/apps/k3b
%{_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_iconsdir}/hicolor/*/apps/k3b.png
%{_datadir}/kde4/services/ServiceMenus/k3b_audiocd_rip.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_cd_copy.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_dvd_copy.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_handle_empty_cd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_handle_empty_dvd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_videodvd_rip.desktop
%{_datadir}/kde4/services/k3bexternalencoder.desktop
%{_datadir}/kde4/services/k3bffmpegdecoder.desktop
%{_datadir}/kde4/services/k3bflacdecoder.desktop
%{_datadir}/kde4/services/k3blameencoder.desktop
%{_datadir}/kde4/services/k3blibsndfiledecoder.desktop
%{_datadir}/kde4/services/k3bmaddecoder.desktop
%{_datadir}/kde4/services/k3boggvorbisdecoder.desktop
%{_datadir}/kde4/services/k3boggvorbisencoder.desktop
%{_datadir}/kde4/services/k3bsetup2.desktop
%{_datadir}/kde4/services/k3bsoxencoder.desktop
%{_datadir}/kde4/services/k3bwavedecoder.desktop
%{_datadir}/kde4/services/kcm_k3bexternalencoder.desktop
%{_datadir}/kde4/services/kcm_k3blameencoder.desktop
%{_datadir}/kde4/services/kcm_k3boggvorbisencoder.desktop
%{_datadir}/kde4/services/videodvd.protocol
%{_datadir}/kde4/servicetypes/k3bplugin.desktop
%{_datadir}/sounds/k3b_*.wav
