Summary:	JIGS - Java Interface for GNUstep
Summary(pl):	JIGS - Interfejs Javy do GNUstepa
Name:		jigs
Version:	1.5.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.gnustep.it/jigs/Download/%{name}-%{version}.tar.gz
# Source0-md5:	76a55f10dfbadf5efce58867dfc7f3c7
URL:		http://www.gnustep.it/jigs/index.html
BuildRequires:	gnustep-base-devel
BuildRequires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gsdir		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
JIGS stands for Java Interface for GnuStep. It is a package allowing
integration between Java and Objective-C. The main purpose of JIGS is
to allow Java programmers to use the GNUstep libraries from Java.

%description -l pl
JIGS to skrót od Java Interface for GnuStep, czyli interfejsu Javy dla
GnuStepa. Jest to pakiet pozwalaj±cy na integracjê miêdzy Jav± a
Objective-C. G³ównym celem JIGS jest umo¿liwienie programistom Javy
u¿ywania bibliotek GNUstepa z poziomu Javy.

%prep
%setup -q

%build
. %{_gsdir}/System/Library/Makefiles/GNUstep.sh

%{__make} \
	OPTFLAG="%{rpmcflags}" \
	JAVA_HOME=%{_libdir}/java \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_gsdir}/System/Library/Makefiles/GNUstep.sh
%{__make} install \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_gsdir}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%{_gsdir}/System/Library/Documentation/Developer/JIGS
%{_gsdir}/System/Library/Headers/%{libcombo}/gnustep/java
%{_gsdir}/System/Library/Libraries/Java
%attr(755,root,root) %{_gsdir}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so*
%{_gsdir}/System/Library/Makefiles/*.make
%{_gsdir}/System/Library/Makefiles/*.template
%attr(755,root,root) %{_gsdir}/System/Library/Makefiles/*.sh
%attr(755,root,root) %{_gsdir}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/WrapCreator
