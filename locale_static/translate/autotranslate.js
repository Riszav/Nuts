document.addEventListener('DOMContentLoaded', function() {
    const translations = [
        { mainFieldId: 'id_answer_ru', targetFieldIds: ['id_answer_en',] },
        { mainFieldId: 'id_question_ru', targetFieldIds: ['id_question_en',]},
        { mainFieldId: 'id_address_ru', targetFieldIds: ['id_address_en',] },
        { mainFieldId: 'id_title_ru', targetFieldIds: ['id_title_en',] },
        { mainFieldId: 'id_description_ru', targetFieldIds: ['id_description_en',] },
        { mainFieldId: 'id_name_ru', targetFieldIds: ['id_name_en',] },
        { mainFieldId: 'id_volume_ru', targetFieldIds: ['id_volume_en',] },
        { mainFieldId: 'id_text_ru', targetFieldIds: ['id_text_en',] },
    ];
    translations.forEach(translation => {
        setupTranslation(translation.mainFieldId, translation.targetFieldIds, '/api/translate/');
    });
});


function setupTranslation(mainFieldId, targetFieldIds, url) {
    const mainField = document.getElementById(mainFieldId);
    const targetFields = targetFieldIds.map(id => document.getElementById(id));
    let timer = null;

    if (mainField && targetFields.every(field => field !== null)) {
        mainField.addEventListener('input', function() {
            clearTimeout(timer);

            timer = setTimeout(() => {
                const textToTranslate = mainField.value.trim();

                if (textToTranslate) {
                    fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify({
                            text_to_translate: textToTranslate,
                            target_language: ['en',]
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data && data.translated_text) {
                            targetFields[0].value = data.translated_text[0];
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                }
            }, 500);
        });
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}