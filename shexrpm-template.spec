Name:           gnome-shell-extension-%{extension_uuid}
Version:        %{extension_version}
Summary:        %{extension_name}
URL:            %{extension_url}
Release:        %(date +%%H.%%M.%%S)
License:        GPLv2 compatible, unknown
Group:          User Interface/Desktops
BuildArch:      noarch
Source0:        %{extension_download_url}

%description
%{extension_description}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extension_uuid}
chmod -R 0667 %{buildroot}%{_datadir}/gnome-shell/extensions/%{extension_uuid}
cp -r --preserve=mode %{buildroot}%{_datadir}/gnome-shell/extensions/%{extension_uuid}/

%files
%defattr(-,root,root,-)
%{_datadir}/gnome-shell/extensions/%{extension_uuid}/
