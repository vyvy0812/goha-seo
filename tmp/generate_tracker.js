const fs = require('fs');
const path = require('path');

const baseDir = "C:\\Users\\MSI\\Documents\\Antigravity-SEO\\Keywords\\Home Credit";

function getFiles(dir, files = []) {
    const list = fs.readdirSync(dir);
    for (const file of list) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            getFiles(fullPath, files);
        } else if (file === 'outline.md') {
            files.push(fullPath);
        }
    }
    return files;
}

const allFiles = getFiles(baseDir);
const fileStats = allFiles.map(f => ({ path: f, mtime: fs.statSync(f).mtime })).sort((a, b) => b.mtime - a.mtime).slice(0, 15);

let md = `# 📚 Danh sách các Outline gần đây nhất\n\n`;
md += `> ⚠️ **LƯU Ý QUAN TRỌNG:** Nếu bạn đang xem file này ở chế độ Preview và bấm link **command** không có phản hồi, đó là do cơ chế bảo mật của VS Code đang chặn các lệnh (command links). \n`;
md += `> 👉 **Cách khắc phục:** Hãy click chuột vào link từ màn hình **CODE (chữ)** thay vì màn hình Preview (giữ phím \`Ctrl\` + click chuột). Hoặc nếu muốn click ngay trong Preview, hãy bấm biểu tượng **🔒 (Security / Shield)** ở trên cùng bên phải thanh menu, và chọn **"Allow insecure local content" / "Allow command links"**.\n\n`;
md += `| Thời gian cập nhật | Thư mục Keyword | File Gốc | Xem trước (Preview) |\n`;
md += `|---|---|---|---|\n`;

for (const item of fileStats) {
    const d = item.mtime;
    // GMT+7
    const localTime = new Date(d.getTime() + 7 * 60 * 60 * 1000);
    const timeStr = localTime.toISOString().replace('T', ' ').substring(0, 19);

    const parts = item.path.split(path.sep);
    const kwFolder = parts[parts.length - 3];

    const fileUrl = "file:///" + item.path.replace(/\\/g, '/');

    // Command args for markdown.showPreviewToSide - passing array with file URI string is the widely supported format
    const arg = encodeURIComponent(JSON.stringify([fileUrl]));
    const previewLink = `command:markdown.showPreviewToSide?${arg}`;

    md += `| ${timeStr} | \`${kwFolder}\` | [📝 Mở File Markdown](${fileUrl}) | [👀 Mở chế độ Preview](${previewLink}) |\n`;
}

fs.writeFileSync(path.join(baseDir, '_Danh_sach_Outline.md'), md, 'utf8');
console.log("Updated tracker with simpler preview links successfully.");
