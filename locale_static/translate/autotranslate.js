document.addEventListener('DOMContentLoaded', function() {
    const translations = [
        { mainFieldId: 'id_answer_ru', targetFieldIds: ['id_answer_en'] },
        { mainFieldId: 'id_question_ru', targetFieldIds: ['id_question_en'] },
        { mainFieldId: 'id_address_ru', targetFieldIds: ['id_address_en'] },
        { mainFieldId: 'id_title_ru', targetFieldIds: ['id_title_en'] },
        { mainFieldId: 'id_description_ru', targetFieldIds: ['id_description_en'] },
        { mainFieldId: 'id_name_ru', targetFieldIds: ['id_name_en'] },
        { mainFieldId: 'id_volume_ru', targetFieldIds: ['id_volume_en'] },
        { mainFieldId: 'id_text_ru', targetFieldIds: ['id_text_en'] },
    ];

    translations.forEach(translation => {
        setupTranslation(translation.mainFieldId, translation.targetFieldIds, '/translate/');
    });

    // Подписка на добавление новых инлайн-форм
    document.body.addEventListener('click', function(event) {
        if (event.target && event.target.classList.contains('add-row')) {
            setTimeout(function() {
                translations.forEach(translation => {
                    setupTranslation(translation.mainFieldId, translation.targetFieldIds, '/translate/');
                });
            }, 500); // Даем время для создания новой формы
        }
    });
});

function getCKEditorInstance(fieldId) {
    const editorElement = document.querySelector(`#${fieldId}`);
    return editorElement ? editorElement.ckeditorInstance : null;
}

function setupTranslation(mainFieldId, targetFieldIds, url) {
    const mainEditorInstance = getCKEditorInstance(mainFieldId);
    const targetEditorInstances = targetFieldIds.map(id => getCKEditorInstance(id));
    let timer = null;

    if (mainEditorInstance && targetEditorInstances.every(instance => instance !== null)) {
        mainEditorInstance.model.document.on('change:data', function() {
            clearTimeout(timer);

            timer = setTimeout(() => {
                const textToTranslate = mainEditorInstance.getData().trim(); // Получаем данные из CKEditor 5

                if (textToTranslate) {
                    fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify({
                            text_to_translate: textToTranslate,
                            target_language: ['en']
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data && data.translated_text) {
                            targetEditorInstances[0].setData(data.translated_text[0]);
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
