const registerVideo = document.getElementById("registerVideo");
const registerCanvas = document.getElementById("registerCanvas");
const registerForm = document.getElementById("registerForm");
const registerMessage = document.getElementById("registerMessage");
const attendanceTable = document.getElementById("attendanceTable");
const totalUsers = document.getElementById("totalUsers");
const presentToday = document.getElementById("presentToday");
const totalRecords = document.getElementById("totalRecords");

async function iniciarCamaraRegistro() {
  if (!registerVideo) return;

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    registerVideo.srcObject = stream;
  } catch (error) {
    registerMessage.textContent = "No se pudo activar la cámara.";
  }
}

function capturarImagenRegistro() {
  registerCanvas.width = registerVideo.videoWidth;
  registerCanvas.height = registerVideo.videoHeight;
  registerCanvas.getContext("2d").drawImage(registerVideo, 0, 0);
  return registerCanvas.toDataURL("image/jpeg", 0.9);
}

if (registerForm) {
  iniciarCamaraRegistro();

  registerForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    try {
      registerMessage.className = "mt-4 text-gray-300";
      registerMessage.textContent = "Registrando usuario...";

      const payload = {
        name: document.getElementById("name").value.trim(),
        code: document.getElementById("code").value.trim(),
        role: document.getElementById("role").value.trim(),
        image_base64: capturarImagenRegistro()
      };

      const data = await apiPost("/register-user", payload);

      registerMessage.className = "mt-4 text-green-400 font-semibold";
      registerMessage.textContent = data.message;
      registerForm.reset();
    } catch (error) {
      registerMessage.className = "mt-4 text-red-400 font-semibold";
      registerMessage.textContent = `Error: ${error.message}`;
    }
  });
}

async function cargarDashboard() {
  if (!attendanceTable) return;

  try {
    const [users, records] = await Promise.all([
      apiGet("/users"),
      apiGet("/get-attendance")
    ]);

    const today = new Date().toISOString().slice(0, 10);
    const todayRecords = records.filter(item => item.attendance_date === today);

    totalUsers.textContent = users.length;
    presentToday.textContent = todayRecords.length;
    totalRecords.textContent = records.length;

    attendanceTable.innerHTML = records.map(item => `
      <tr class="border-b border-white/10">
        <td class="py-3">${item.name}</td>
        <td class="py-3">${item.code}</td>
        <td class="py-3">${item.role}</td>
        <td class="py-3">${item.attendance_date}</td>
        <td class="py-3">${item.status}</td>
        <td class="py-3">${item.distance_meters ?? "-"} m</td>
      </tr>
    `).join("") || `
      <tr><td class="py-4 text-gray-400" colspan="6">Todavía no hay asistencias registradas.</td></tr>
    `;
  } catch (error) {
    attendanceTable.innerHTML = `
      <tr><td class="py-4 text-red-400" colspan="6">Error cargando dashboard: ${error.message}</td></tr>
    `;
  }
}

cargarDashboard();
