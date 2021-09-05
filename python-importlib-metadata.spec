%global debug_package %{nil}

Name: python-importlib-metadata
Epoch: 100
Version: 4.8.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Library to access the metadata for a Python package
License: Apache-2.0
URL: https://github.com/python/importlib_metadata/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Library to access the metadata for a Python package. This package
supplies third-party access to the functionality of importlib.metadata
including improvements added to subsequent Python versions.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-importlib-metadata
Summary: Library to access the metadata for a Python package
Requires: python3
Requires: python3-typing-extensions >= 3.6.4
Requires: python3-zipp >= 0.5
Provides: python3-importlib-metadata = %{epoch}:%{version}-%{release}
Provides: python3dist(importlib-metadata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-importlib-metadata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(importlib-metadata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-importlib-metadata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(importlib-metadata) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-importlib-metadata
Library to access the metadata for a Python package. This package
supplies third-party access to the functionality of importlib.metadata
including improvements added to subsequent Python versions.

%files -n python%{python3_version_nodots}-importlib-metadata
%license LICENSE
%{python3_sitelib}/importlib_metadata*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-importlib-metadata
Summary: Library to access the metadata for a Python package
Requires: python3
Requires: python3-typing-extensions >= 3.6.4
Requires: python3-zipp >= 0.5
Provides: python3-importlib-metadata = %{epoch}:%{version}-%{release}
Provides: python3dist(importlib-metadata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-importlib-metadata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(importlib-metadata) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-importlib-metadata = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(importlib-metadata) = %{epoch}:%{version}-%{release}

%description -n python3-importlib-metadata
Library to access the metadata for a Python package. This package
supplies third-party access to the functionality of importlib.metadata
including improvements added to subsequent Python versions.

%files -n python3-importlib-metadata
%license LICENSE
%{python3_sitelib}/importlib_metadata*
%endif

%changelog
