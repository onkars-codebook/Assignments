function calculateScore(event) {
    event.preventDefault();

    const english = parseInt(document.getElementById('english').value);
    const marathi = parseInt(document.getElementById('marathi').value);
    const science = parseInt(document.getElementById('science').value);
    const mathematics = parseInt(document.getElementById('mathematics').value);

    const totalScore = english + marathi + science + mathematics;

    const percentage = (totalScore / 400) * 100;

    let grade;
    if (percentage >= 90) {
        grade = 'A';
    } else if (percentage >= 80) {
        grade = 'B';
    } else if (percentage >= 70) {
        grade = 'C';
    } else if (percentage >= 60) {
        grade = 'D';
    } else {
        grade = 'F';
    }

    const scores = { English: english, Marathi: marathi, Science: science, Mathematics: mathematics };
    const bestSubject = Object.keys(scores).reduce((a, b) => (scores[a] > scores[b] ? a : b));

    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = `
        <p><strong>Total Score:</strong> <ins>${totalScore}</ins></p>
        <p><strong>Percentage:</strong> <ins>${percentage.toFixed(2)}%</ins></p>
        <p><strong>Grade:</strong> <ins>${grade}</ins></p>
        <p><strong>Best Subject:</strong> <ins>${bestSubject}</ins></p>
    `;
}

document.querySelector('form').addEventListener('submit', calculateScore);