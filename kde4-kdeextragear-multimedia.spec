%define		orgname kdeextragear-multimedia
%define		snap 856389
Summary:	extra multimedia
Summary(pl.UTF-8):	Dodatkowe programy multimedialne
Name:		kde4-kdeextragear-multimedia
Version:	4.1.64
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/%{orgname}-%{snap}.tar.bz2
# Source0-md5:	93072b1804d00abd1b808199d203b8e8
URL:		http://extragear.kde.org/apps/kipi/
Patch0:		%{name}-NJB.patch
BuildRequires:	kde4-kdemultimedia-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libgpod-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libnjb-devel
BuildRequires:	mpeg4ip-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	taglib-devel
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
Suggests:	cdrdao
Suggests:	cdrtools
Suggests:	dvd+rw-tools

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
%patch0 -p0

%build
install -d {amarok/build,k3b/build}
cd amarok/build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

cd ../../k3b/build
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

%post	-n kde4-amarok	-p /sbin/ldconfig
%postun	-n kde4-amarok	-p /sbin/ldconfig

%post	-n kde4-k3b	-p /sbin/ldconfig
%postun	-n kde4-k3b	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde4-amarok
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amarok
%attr(755,root,root) %{_bindir}/amarokcollectionscanner
%attr(755,root,root) %{_bindir}/amarokmp3tunesharmonydaemon
%attr(755,root,root) %{_bindir}/amarok_afttagger
%attr(755,root,root) %{_libdir}/kde4/amarok_containment_context.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_currenttrack.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_lastfmevents.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_lyrics.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_serviceinfo.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_video.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_wikipedia.so
%attr(755,root,root) %{_libdir}/kde4/amarok_data_engine_cloud.so
%attr(755,root,root) %{_libdir}/kde4/amarok_data_engine_current.so
%attr(755,root,root) %{_libdir}/kde4/amarok_data_engine_lastfm.so
%attr(755,root,root) %{_libdir}/kde4/amarok_data_engine_lyrics.so
%attr(755,root,root) %{_libdir}/kde4/amarok_data_engine_service.so
%attr(755,root,root) %{_libdir}/kde4/amarok_data_engine_wikipedia.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_ampache.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_jamendo.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_lastfm.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_magnatunestore.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_mp3tunes.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_opmldirectory.so
%attr(755,root,root) %{_libdir}/kde4/amarok_service_shoutcast.so
%attr(755,root,root) %{_libdir}/kde4/kcm_amarok_service_ampache.so
%attr(755,root,root) %{_libdir}/kde4/kcm_amarok_service_lastfm.so
%attr(755,root,root) %{_libdir}/kde4/kcm_amarok_service_magnatunestore.so
%attr(755,root,root) %{_libdir}/kde4/kcm_amarok_service_mp3tunes.so
%attr(755,root,root) %{_libdir}/kde4/libamarok_collection-daapcollection.so
%attr(755,root,root) %{_libdir}/kde4/libamarok_collection-sqlcollection.so
%attr(755,root,root) %{_libdir}/kde4/amarok_context_applet_albums.so
%attr(755,root,root) %{_libdir}/kde4/libamarok_collection-ipodcollection.so
%attr(755,root,root) %{_libdir}/kde4/libamarok_collection-mtpcollection.so
%attr(755,root,root) %{_libdir}/libamarok_taglib.so
%attr(755,root,root) %{_libdir}/libamaroklib.so
%attr(755,root,root) %{_libdir}/libamarokplasma.so
%attr(755,root,root) %{_libdir}/libamarokpud.so
%attr(755,root,root) %{_libdir}/libamarokpud.so.1
%attr(755,root,root) %{_libdir}/libamarokpud.so.1.0.0
%attr(755,root,root) %{_libdir}/libk3b.so
%attr(755,root,root) %{_libdir}/libk3bdevice.so
%attr(755,root,root) %ghost %{_libdir}/libamarok_taglib.so.1
%attr(755,root,root) %{_libdir}/libamarok_taglib.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libamaroklib.so.1
%attr(755,root,root) %{_libdir}/libamaroklib.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libamarokplasma.so.2
%attr(755,root,root) %{_libdir}/libamarokplasma.so.2.0.0
%attr(755,root,root) %{_libdir}/strigi/strigita_audible.so
%attr(755,root,root) %{_libdir}/strigi/strigita_mp4.so
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libqtscript_core.so
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libqtscript_gui.so
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libqtscript_network.so
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libqtscript_sql.so
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libqtscript_uitools.so
%attr(755,root,root) %{_libdir}/kde4/plugins/script/libqtscript_xml.so

%{_desktopdir}/kde4/amarok.desktop
%{_datadir}/apps/amarok
%{_datadir}/apps/desktoptheme/Amarok-Mockup
%{_datadir}/apps/desktoptheme/amarok-default.desktop
%{_datadir}/apps/desktoptheme/default/widgets
%{_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/config.kcfg/amarok.kcfg
%{_datadir}/config/amarok.knsrc
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.player.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.root.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer.tracklist.xml
%{_iconsdir}/hicolor/*x*/apps/amarok.png
%{_datadir}/kde4/services/ServiceMenus/amarok_append.desktop
%{_datadir}/kde4/services/amarok-context-applet-albums.desktop
%{_datadir}/kde4/services/amarok_collection-ipodcollection.desktop
%{_datadir}/kde4/services/amarok_collection-mtpcollection.desktop
%{_datadir}/kde4/services/amarok-containment-context.desktop
%{_datadir}/kde4/services/amarok-context-applet-currenttrack.desktop
%{_datadir}/kde4/services/amarok-context-applet-lastfmevents.desktop
%{_datadir}/kde4/services/amarok-context-applet-lyrics.desktop
%{_datadir}/kde4/services/amarok-context-applet-serviceinfo.desktop
%{_datadir}/kde4/services/amarok-context-applet-video.desktop
%{_datadir}/kde4/services/amarok-context-applet-wikipedia.desktop
%{_datadir}/kde4/services/amarok-data-engine-cloud.desktop
%{_datadir}/kde4/services/amarok-data-engine-current.desktop
%{_datadir}/kde4/services/amarok-data-engine-lastfm.desktop
%{_datadir}/kde4/services/amarok-data-engine-lyrics.desktop
%{_datadir}/kde4/services/amarok-data-engine-service.desktop
%{_datadir}/kde4/services/amarok-data-engine-wikipedia.desktop
%{_datadir}/kde4/services/amarok_collection-daapcollection.desktop
%{_datadir}/kde4/services/amarok_collection-sqlcollection.desktop
%{_datadir}/kde4/services/amarok_service_ampache.desktop
%{_datadir}/kde4/services/amarok_service_ampache_config.desktop
%{_datadir}/kde4/services/amarok_service_jamendo.desktop
%{_datadir}/kde4/services/amarok_service_lastfm.desktop
%{_datadir}/kde4/services/amarok_service_lastfm_config.desktop
%{_datadir}/kde4/services/amarok_service_magnatunestore.desktop
%{_datadir}/kde4/services/amarok_service_magnatunestore_config.desktop
%{_datadir}/kde4/services/amarok_service_mp3tunes.desktop
%{_datadir}/kde4/services/amarok_service_mp3tunes_config.desktop
%{_datadir}/kde4/services/amarok_service_opmldirectory.desktop
%{_datadir}/kde4/services/amarok_service_shoutcast.desktop
%{_datadir}/kde4/servicetypes/amarok_context_applet.desktop
%{_datadir}/kde4/servicetypes/amarok_data_engine.desktop
%{_datadir}/kde4/servicetypes/amarok_plugin.desktop

%files -n kde4-k3b
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/k3b
%attr(755,root,root) %{_bindir}/k3bsetup
%attr(755,root,root) %{_libdir}/kde4/k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bmaddecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisdecoder.so
%attr(755,root,root) %{_libdir}/kde4/k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bsoxencoder.so
%attr(755,root,root) %{_libdir}/kde4/k3bwavedecoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bexternalencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3blameencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3boggvorbisencoder.so
%attr(755,root,root) %{_libdir}/kde4/kcm_k3bsetup2.so
%attr(755,root,root) %{_libdir}/kde4/kio_videodvd.so
%attr(755,root,root) %ghost %{_libdir}/libk3b.so.4
%attr(755,root,root) %{_libdir}/libk3b.so.4.0.0
%attr(755,root,root) %ghost %{_libdir}/libk3bdevice.so.6
%attr(755,root,root) %{_libdir}/libk3bdevice.so.6.0.0
%attr(755,root,root) %{_libdir}/kde4/k3blibsndfiledecoder.so
%{_desktopdir}/kde4/k3b.desktop
%{_datadir}/apps/k3b
%{_iconsdir}/hicolor/*x*/apps/k3b.png
%{_datadir}/kde4/services/ServiceMenus/k3b_audiocd_rip.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_cd_copy.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_dvd_copy.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_handle_empty_cd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_handle_empty_dvd.desktop
%{_datadir}/kde4/services/ServiceMenus/k3b_videodvd_rip.desktop
%{_datadir}/kde4/services/k3bexternalencoder.desktop
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
%{_datadir}/sounds/k3b*.wav
