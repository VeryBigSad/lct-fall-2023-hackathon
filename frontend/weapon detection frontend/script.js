document.addEventListener('DOMContentLoaded', () => {
  const mainFrame = document.getElementById('main');
  const mainFrameBtn = document.querySelector('.add-section__btn');
  let files = [];
  function createSecondFrame() {
    const secondFrame = document.createElement('div');
    secondFrame.classList.add('secondframe');
    const directories = document.createElement('div');
    directories.classList.add('secondframe__directories');
    const directoriesH = document.createElement('h2');
    directoriesH.textContent = 'Detections';
    directoriesH.classList.add('directories__heading');
    directories.append(directoriesH);
    const viewZone = document.createElement('div');
    viewZone.classList.add('secondframe__viewzone');
    const tabs = document.createElement('div');
    tabs.classList.add('secondframe__tabs');
    const tabsList = document.createElement('ul');
    tabsList.classList.add('secondframe__tabs-list');
    const tabContent = document.createElement('div');
    tabContent.classList.add('secondframe__tabcontent');
    // const tabContentDetectionsSection = document.createElement('div');
    // const tabContentDetections = document.createElement('ul'); 
    for (let i = 0; i < files.length; i++) {
      const tabItem = document.createElement('li');
      tabItem.classList.add('secondframe__tabs-item');
      const cross = document.createElement('span');
      cross.classList.add('secondframe__tabs-cross');      
      inum = i + 1;
      tabItem.textContent = 'Процесс ' + inum;
      tabItem.append(cross);
      cross.addEventListener('click', () => {
        tabItem.remove();
      }) 
      tabsList.append(tabItem);
    }
    for (let i = 0; i < files.length; i++) {
      const tabContentVideoBlock = document.createElement('div');
      tabContentVideoBlock.classList.add('secondframe__tabcontent-videoblock')
      const tabContentVideo = document.createElement('video');
      tabContentVideo.classList.add('secondframe__tabcontent-video');
      tabContentVideo.controls = true;
      tabContentVideo.src = URL.createObjectURL(files[i]);

      tabContentVideoBlock.append(tabContentVideo);
      tabContent.append(tabContentVideoBlock);
    }
    tabContent.children[0].classList.add('secondframe__tabcontent-videoblock--active');
    tabsList.children[0].classList.add('secondframe__tabs-item--active');
    for (let i = 0; i < tabsList.children.length; i++) {
      tabsList.children[i].addEventListener('click', () => {
        for (let x = 0; x < tabsList.children.length; x++) {
          tabsList.children[x].classList.remove('secondframe__tabs-item--active');
          tabContent.children[x].classList.remove('secondframe__tabcontent-videoblock--active');
        }
        tabsList.children[i].classList.add('secondframe__tabs-item--active');
        tabContent.children[i].classList.add('secondframe__tabcontent-videoblock--active');
      })
    }
    tabs.append(tabsList);
    viewZone.append(tabs);
    secondFrame.append(directories);
    secondFrame.append(viewZone);
    viewZone.append(tabContent);  
    document.body.append(secondFrame);
    return;
  };
  function createAddFileWindow() {
    const window = document.createElement('div');
    window.classList.add('add-file-window');
    const fileInput = document.createElement('input');
    fileInput.classList.add('add-file-window-input');
    fileInput.type = 'file';
    fileInput.accept = 'video/mp4', 'video/avi';
    const cross = document.createElement('div');
    cross.classList.add('add-file-window-cross')
    const startBtn = document.createElement('button');
    startBtn.textContent = 'Начать работу';
    startBtn.classList.add('add-file-window-btn')
    const videoNum = document.createElement('span');
    videoNum.classList.add('add-file-window-span');
    window.append(cross);
    window.append(fileInput);
    window.append(startBtn);
    window.append(videoNum);
    mainFrame.append(window);
    cross.addEventListener('click', () => {
      files = [];
      window.remove()
    });
    fileInput.addEventListener('change', () => {
      for (let i=0; i<fileInput.files.length; i++) {
        files.push(fileInput.files[i]);
      }
      videoNum.textContent = 'Загружено ' + files.length + ' видео'; 
    });
    return {cross, startBtn,};
  }
  mainFrameBtn.addEventListener('click', () => {
    const addFileWindow = createAddFileWindow().startBtn;
    addFileWindow.addEventListener('click', () => {
      if (files.length>0) {
        createSecondFrame();
      } else {
        alert('Вы еще не выбрали файл!');
      }
    })    
  });
})