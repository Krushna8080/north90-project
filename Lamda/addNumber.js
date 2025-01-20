// File: addNumbers.js
exports.handler = async (event) => {
    const { num1, num2 } = event;
    
    if (typeof num1 !== "number" || typeof num2 !== "number") {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: "Invalid input. Both num1 and num2 should be numbers." }),
        };
    }

    const result = num1 + num2;

    return {
        statusCode: 200,
        body: JSON.stringify({ result }),
    };
};

// Test Locally
if (require.main === module) {
    (async () => {
        const result = await exports.handler({ num1: 10, num2: 20 });
        console.log(result);
    })();
}
