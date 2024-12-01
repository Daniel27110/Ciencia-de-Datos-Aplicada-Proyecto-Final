// Function to handle group prediction
async function hacerPrediccionGrupal() {
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];
    if (!file) {
       alert("Por favor, seleccione un archivo CSV.");
       return;
    }
 
    const reader = new FileReader();
    reader.onload = async function (e) {
       const csvData = e.target.result;
       const rows = csvData.split('\n').slice(1); // Skip header row
       const jsonData = rows.map(row => {
          const values = row.split(',');
          return {
             "ESTRATO": parseInt(values[0]),
             "SEMESTRE": parseInt(values[1]),
             "PROMEDIOSEMESTRE": parseFloat(values[2]),
             "EDAD2": parseInt(values[3]),
             "PROGRAMA": values[4].trim(),
             "GENERO": values[5].trim(),
             "CIUDADRESIDENCIA": values[6].trim(),
             "CIUDADNACIMIENTO": values[7].trim()
          };
       });
 
       const response = await fetch('/predict-group', {
          method: 'POST',
          headers: {
             'Content-Type': 'application/json',
          },
          body: JSON.stringify(jsonData)
       });
 
       if (!response.ok) {
          console.error('Error al obtener la respuesta:', response.status);
          return;
       }
 
       const result = await response.json();
       console.log("Resultado recibido del servidor:", result); // Para depuración
 
       // Process and display the results
       const labels = result.map((_, index) => `Estudiante ${index + 1}`);
       const desertores = result.map(r => r.prediccion === 0 ? 1 : 0);
       const noDesertores = result.map(r => r.prediccion === 1 ? 1 : 0);
 
       // Bar Chart
       const ctxBar = document.getElementById('graficoGrupalPrediccion').getContext('2d');
       new Chart(ctxBar, {
          type: 'bar',
          data: {
             labels: labels,
             datasets: [
                {
                   label: 'Desertores',
                   data: desertores,
                   backgroundColor: 'rgba(255, 99, 132, 0.7)',
                },
                {
                   label: 'No Desertores',
                   data: noDesertores,
                   backgroundColor: 'rgba(54, 162, 235, 0.7)',
                }
             ]
          },
          options: {
             responsive: true,
             plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Predicción de Deserción Estudiantil' }
             },
             scales: {
                x: { title: { display: true, text: 'Estudiantes' } },
                y: { title: { display: true, text: 'Número de Estudiantes' } }
             }
          }
       });
 
       // Horizontal Bar Chart
       const ctxHorizontalBar = document.getElementById('graficoHorizontal').getContext('2d');
       new Chart(ctxHorizontalBar, {
          type: 'horizontalBar',
          data: {
             labels: labels,
             datasets: [
                {
                   label: 'Desertores',
                   data: desertores,
                   backgroundColor: 'rgba(255, 99, 132, 0.7)',
                },
                {
                   label: 'No Desertores',
                   data: noDesertores,
                   backgroundColor: 'rgba(54, 162, 235, 0.7)',
                }
             ]
          },
          options: {
             responsive: true,
             plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Predicción de Deserción Estudiantil (Horizontal)' }
             },
             scales: {
                x: { title: { display: true, text: 'Número de Estudiantes' } },
                y: { title: { display: true, text: 'Estudiantes' } }
             }
          }
       });
 
       // Pie Chart
       const ctxPie = document.getElementById('graficoPie').getContext('2d');
       new Chart(ctxPie, {
          type: 'pie',
          data: {
             labels: ['Desertores', 'No Desertores'],
             datasets: [{
                data: [desertores.reduce((a, b) => a + b, 0), noDesertores.reduce((a, b) => a + b, 0)],
                backgroundColor: ['rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)'],
             }]
          },
          options: {
             responsive: true,
             plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Proporción de Deserción Estudiantil' }
             }
          }
       });
 
       // Line Chart for Average Scores
       const avgDesertores = desertores.reduce((a, b) => a + b, 0) / desertores.length || 0;
       const avgNoDesertores = noDesertores.reduce((a, b) => a + b, 0) / noDesertores.length || 0;
       const ctxLine = document.getElementById('graficoLine').getContext('2d');
       new Chart(ctxLine, {
          type: 'line',
          data: {
             labels: ['Desertores', 'No Desertores'],
             datasets: [{
                label: 'Promedio de Estudiantes',
                data: [avgDesertores, avgNoDesertores],
                backgroundColor: 'rgba(75, 192, 192, 0.7)',
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
             }]
          },
          options: {
             responsive: true,
             plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Promedio de Deserción Estudiantil' }
             },
             scales: {
                x: { title: { display: true, text: 'Categoría' } },
                y: { title: { display: true, text: 'Promedio' } }
             }
          }
       });
 
       // Additional Charts
       // Scatter Plot for Age vs. Average Semester Score
       const ctxScatter = document.getElementById('graficoScatter').getContext('2d');
       new Chart(ctxScatter, {
          type: 'scatter',
          data: {
             datasets: [
                {
                   label: 'Desertores',
                   data: result.filter(r => r.prediccion === 0).map(r => ({ x: r.EDAD2, y: r.PROMEDIOSEMESTRE })),
                   backgroundColor: 'rgba(255, 99, 132, 0.7)',
                },
                {
                   label: 'No Desertores',
                   data: result.filter(r => r.prediccion === 1).map(r => ({ x: r.EDAD2, y: r.PROMEDIOSEMESTRE })),
                   backgroundColor: 'rgba(54, 162, 235, 0.7)',
                }
             ]
          },
          options: {
             responsive: true,
             plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Edad vs. Promedio Semestral' }
             },
             scales: {
                x: { title: { display: true, text: 'Edad' } },
                y: { title: { display: true, text: 'Promedio Semestral' } }
             }
          }
       });
 
       // Radar Chart for Program Distribution
       const programs = [...new Set(result.map(r => r.PROGRAMA))];
       const programDesertores = programs.map(program => result.filter(r => r.PROGRAMA === program && r.prediccion === 0).length);
       const programNoDesertores = programs.map(program => result.filter(r => r.PROGRAMA === program && r.prediccion === 1).length);
       const ctxRadar = document.getElementById('graficoRadar').getContext('2d');
       new Chart(ctxRadar, {
          type: 'radar',
          data: {
             labels: programs,
             datasets: [
                {
                   label: 'Desertores',
                   data: programDesertores,
                   backgroundColor: 'rgba(255, 99, 132, 0.7)',
                },
                {
                   label: 'No Desertores',
                   data: programNoDesertores,
                   backgroundColor: 'rgba(54, 162, 235, 0.7)',
                }
             ]
          },
          options: {
             responsive: true,
             plugins: {
                legend: { position: 'top' },
                title: { display: true, text: 'Distribución de Programas' }
             },
             scales: {
                r: { angleLines: { display: false }, suggestedMin: 0 }
             }
          }
       });
    };
    reader.readAsText(file);
 }