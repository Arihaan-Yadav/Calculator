#!/bin/bash
set -eu

launcher_dir=$(cd "$(dirname "$0")" && pwd)
project_dir=$(cd "$launcher_dir/.." && pwd)
chmod +x "$launcher_dir/open.sh" "$launcher_dir/open.command"

case "$(uname -s)" in
    Darwin)
        desktop_dir="$HOME/Desktop"
        app_dir="$desktop_dir/Calculator.app"
        icon_path="/System/Applications/Calculator.app/Contents/Resources/AppIcon.icns"
        if [ ! -f "$icon_path" ]; then
            icon_path="/Applications/Calculator.app/Contents/Resources/AppIcon.icns"
        fi
        if [ ! -f "$icon_path" ]; then
            echo "Could not find the macOS Calculator app icon." >&2
            exit 1
        fi

        mkdir -p "$app_dir/Contents/MacOS" "$app_dir/Contents/Resources"
        cp "$icon_path" "$app_dir/Contents/Resources/Calculator.icns"
        cat > "$app_dir/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>Calculator</string>
    <key>CFBundleDisplayName</key>
    <string>Calculator</string>
    <key>CFBundleIdentifier</key>
    <string>local.calculator.project</string>
    <key>CFBundleExecutable</key>
    <string>Calculator</string>
    <key>CFBundleIconFile</key>
    <string>Calculator</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
</dict>
</plist>
PLIST
        printf '%s\n' '#!/bin/sh' \
            "PROJECT_DIR=$(printf '%q' "$project_dir")" \
            'exec /usr/bin/open -a Terminal "$PROJECT_DIR/open_app/open.command"' \
            > "$app_dir/Contents/MacOS/Calculator"
        chmod +x "$app_dir/Contents/MacOS/Calculator"
        echo "Created $app_dir"
        ;;
    Linux)
        if command -v xdg-user-dir >/dev/null 2>&1; then
            desktop_dir=$(xdg-user-dir DESKTOP)
        else
            desktop_dir="$HOME/Desktop"
        fi
        if [ -z "$desktop_dir" ] || [ ! -d "$desktop_dir" ]; then
            desktop_dir="$HOME/.local/share/applications"
        fi
        mkdir -p "$desktop_dir"

        launcher_path="$launcher_dir/open.sh"
        escaped_launcher=$(printf '%s' "$launcher_path" | sed 's/\\/\\\\/g; s/"/\\"/g; s/\$/\\$/g; s/`/\\`/g')
        cat > "$desktop_dir/Calculator.desktop" <<DESKTOP
[Desktop Entry]
Type=Application
Name=Calculator
Comment=Open the Calculator project
Exec=/usr/bin/env bash "$escaped_launcher"
Icon=accessories-calculator
Terminal=true
Categories=Utility;
DESKTOP
        chmod +x "$desktop_dir/Calculator.desktop"
        echo "Created $desktop_dir/Calculator.desktop"
        ;;
    *)
        echo "This shortcut setup supports macOS and Linux." >&2
        exit 1
        ;;
esac
