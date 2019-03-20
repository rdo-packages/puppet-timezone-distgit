%{!?upstream_version: %global upstream_version %{version}}
%define upstream_name puppet-timezone


Name:           puppet-timezone
Version:        5.1.1
Release:        1%{?dist}
Summary:        Manage timezone settings via Puppet.
License:        ASL 2.0

URL:            https://github.com/saz/puppet-timezone

Source0:        https://github.com/saz/%{upstream_name}/archive/v%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Manage timezone settings via Puppet.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/



%files
%{_datadir}/openstack-puppet/modules/timezone/


%changelog
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 5.1.1-1
- Update to 5.1.1



