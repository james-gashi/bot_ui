/**
 * @typedef {import('../../frontend/node_modules/botasaurus-controls/dist/index').Controls} Controls
 */

/**
 * @param {Controls} controls
 */
function getInput(controls) {
    controls
        // Render a Link Input
        .link('link', { isRequired: true, defaultValue: "https://www.omkar.cloud/" })
        //.section('tag', {isRequired: true, defaultValue: "h1"})
        .section("HTML Tag Setter", (section) => {
            section.text('tag', {
                placeholder: "h1",
                label: 'HTML tag to search by',
                helpText: 'Enter your HTML tag.',
            })
        })
}
