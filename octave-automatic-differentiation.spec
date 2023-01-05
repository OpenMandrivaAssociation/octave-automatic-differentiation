%global octpkg automatic-differentiation

Summary:	Automatic-Differentiation for Octave
Name:		octave-automatic-differentiation
Version:	1.0.0
Release:	1
Source0:	https://github.com/StevenWaldrip/Automatic-Differentiation/archive/%{version}/automatic-differentiation-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/automatic-differentiation/
BuildArch:	noarch

BuildRequires:	octave-devel > 5.1.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Automatic-Differentiation for Octave.

%files
%license COPYING
%doc README.md
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -n Automatic-Differentiation-%{version}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

