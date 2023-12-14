async function createText(event) {
            event.preventDefault();

            const inputText = document.getElementById('main-text').value;

            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: inputText })
            });

            const data = await response.json();

            // Display the generated text
            const generatedText = document.getElementById('final-text');
            generatedText.innerText = data.generated_text[0].generated_text;
        }

        // Attach the form submission event listener
        const form = document.querySelector('form');
        form.addEventListener('submit', createText);