const fs = require('fs');
const path = require('path');

const problemsDir = path.join(__dirname, './problems-src');
const outputFile = path.join(__dirname, './problemsData.json');

const files = fs.readdirSync(problemsDir);

const data = files.map((file, index) => {
  const filePath = path.join(problemsDir, file);
  const content = fs.readFileSync(filePath, 'utf-8').trim();
  const questionTitle = path.basename(file, path.extname(file));

  return {
    number: (index + 1).toString(),
    question: questionTitle,
    solution: content,
  };
});

fs.writeFileSync(outputFile, JSON.stringify(data, null, 2));
console.log('Data generated successfully.');
