const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = {};
  }

  async readFile() {
    try {
      const content = await fs.promises.readFile(this.filePath, 'utf8');
      return content;
    } catch (error) {
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  parseData(content) {
    const lines = content.split('\n');
    lines.forEach((line) => {
      const [key, value] = line.split('=');
      this.data[key.trim()] = value.trim();
    });
    return this.data;
  }

  async parseFile() {
    const content = await this.readFile();
    return this.parseData(content);
  }
}

module.exports = Parser;