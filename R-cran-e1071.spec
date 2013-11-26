%define		fversion	%(echo %{version} |tr r -)
%define		modulename	e1071
Summary:	Misc Functions of the Department of Statistics (e1071), TU Wien
Summary(pl.UTF-8):	Różne funkcje Wydziału Statystyki (e1071) Politechniki Wiedeńskiej
Name:		R-cran-%{modulename}
Version:	1.6r1
Release:	2
License:	GPL v2. See COPYRIGHT.svm.cpp for the copyright of the svm C++ code.
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	cdc77694de66523f05634f58b0eb3128
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions for latent class analysis, short time Fourier transform,
fuzzy clustering, support vector machines, shortest path computation,
bagged clustering, naive Bayes classifier, ...

%description -l pl.UTF-8
Funkcje do analizy klas, szybkiej transformaty Fouriera, rozmytego
klastrowania, obsługi maszyn wektorowych, obliczenia najkrótszych
ścieżek, naiwnej klasyfikacji Bayesa...

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README}
%{_libdir}/R/library/%{modulename}
