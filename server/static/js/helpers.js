/*  Copyright (c) Microsoft Corporation. All rights reserved.
    Licensed under the MIT License. */

/* global $ */

function getImmersiveReaderTokenAsync() {
    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/immerse_token',
            type: 'POST',
            contentType: 'text/plain',
            success: token => {
                resolve(token);
            },
            error: err => {
                console.log('Error in getting token!', err);
                reject(err);
            }
        });
    });
}
