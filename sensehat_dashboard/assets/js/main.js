// Some easy standards
const dbConfig = {
	collection: 'raspberry',
	document: 'collectie',
};

const app = {
	init() {
		// Initializing the firebase app
		firebase.initializeApp(firebaseConfig);
		this._db = firebase.firestore();

		// Logging the collection as a test
		this._db.collection('raspberry').doc('collectie').get().then((doc) => {
			const data = doc.data();
			console.log(data);
		});

		this._matrix = {
            isOn: false, color: {value: '#000000', type: 'hex'}
        };

		this.cacheDOMElements();
		this.cacheDOMEvents();
	},

	cacheDOMElements() {
		// The color picker
		this.colorPicker = document.getElementById('colorPicker');
		// On/off matrix
		this.toggleMatrix = document.getElementById('toggleMatrix');
		// Submit
		this.btnChange = document.getElementById('btnChange');
	},

	cacheDOMEvents() {
		this.btnChange.addEventListener('click', (e) => {
			e.preventDefault();

			// Adding the values to our object
			this._matrix.color.value = this.colorPicker.value;
			this._matrix.isOn = this.toggleMatrix.checked;

			this.updateFirebase();
		});
	},

	updateFirebase() {
		this._db.collection(dbConfig.collection).doc(dbConfig.document).set({
			matrix: this._matrix
		}, {merge: true});
	}
};

app.init();

